#include "ros/ros.h"
#include "glad/glad.h"
#include "sensor_msgs/Joy.h"
#include <GLFW/glfw3.h>
#include "Game.h"
#include "gl_frontend.h"
#include <iostream>
#include <chrono>
#include <thread>
#include <game/Player.h>
#include <game/GameState.h>
#include <game/Enemy.h>
#include <game/Projectile.h>
#include <game/Explosion.h>
#include <sensor_msgs/Image.h>

// #include "game/Enemy.h"
using namespace mrsd;

void setupScenarioEasy(Game&);
void setupScenarioMedium(Game&);
void setupScenarioHard(Game&);
void setupScenarioVeryHard(Game&);
void setupScenarioImpossible(Game&);


class GameNode {
	public:
		float curr_dir = 0.0f;
		ros::NodeHandle nh_;
		GameNode() : nh_(), joy_subscriber_(nh_.subscribe("joy", 10, &GameNode::joyCallback, this)) {
			// Initialize any variables or setup you need here
		}

		void joyCallback(const sensor_msgs::Joy::ConstPtr& joy_msg) {
			curr_dir = joy_msg->axes[0];
			
		}

		
	private:
		ros::Subscriber joy_subscriber_;
};

void publishImage(ros::Publisher& pub, int width, int height) {
    sensor_msgs::Image image_msg;
    image_msg.width = width;
    image_msg.height = height;
    image_msg.encoding = "rgb8"; // Adjust encoding as needed
    image_msg.step = 3 * width;
    image_msg.data.resize(3 * width * height);

    // Read pixel data from framebuffer
    glReadBuffer(GL_FRONT);
    glReadPixels(0, 0, width, height, GL_RGB, GL_UNSIGNED_BYTE, image_msg.data.data());
	// Flip image vertically
    std::vector<uint8_t> flipped_data(3 * width * height);
    for (int y = 0; y < height; ++y) {
        int flipped_y = height - y - 1;
        std::memcpy(&flipped_data[flipped_y * 3 * width], &image_msg.data[y * 3 * width], 3 * width);
    }
    
    // Copy flipped data back to the image message
    std::memcpy(image_msg.data.data(), flipped_data.data(), 3 * width * height);

    // Publish image message
    pub.publish(image_msg);
    // Publish image message
    pub.publish(image_msg);
}

void update_ros_game(Game& g, ros::Publisher& pub)
{
	game::GameState msg;
	msg.gravity = g.getGravity();
	msg.w = g.getWidth();
	msg.h = g.getHeight();
	msg.time_step = g.getTimeStep();
	msg.time = g.getGameTime();

	if(!g.getPlayers().empty())
	{
		game::Player player_msg;
		player_msg.x = g.getPlayers()[0]->x;
		player_msg.dead = g.getPlayers()[0]->dead;
		msg.players.push_back(player_msg);
	}
	if(!g.getEnemies().empty())
	{
		for(auto& e : g.getEnemies())
		{
			game::Enemy enemy_msg;
			enemy_msg.x = e.x;
			enemy_msg.y = e.y;
			enemy_msg.minAngle = e.minAngle;
			enemy_msg.maxAngle = e.maxAngle;
			enemy_msg.minForce = e.minForce;
			enemy_msg.maxForce = e.maxForce;
			enemy_msg.firingSpeed = e.firingSpeed;
			enemy_msg.firingRandomness = e.firingRandomness;
			enemy_msg.turretSpeed = e.turretSpeed;
			msg.enemies.push_back(enemy_msg);
		}
	}
	if(!g.getProjectiles().empty())
	{
		for(auto& p : g.getProjectiles())
		{
			game::Projectile projectile_msg;
			projectile_msg.x = p.x;
			projectile_msg.y = p.y;
			projectile_msg.vx = p.vx;
			projectile_msg.vy = p.vy;
			msg.projectiles.push_back(projectile_msg);
		}
	}
	if(!g.getExplosions().empty())
	{
		for(auto& e : g.getExplosions())
		{
			game::Explosion explosion_msg;
			explosion_msg.x = e.x;
			explosion_msg.y = e.y;
			explosion_msg.time = e.time;
			msg.explosions.push_back(explosion_msg);
		}
	}
	pub.publish(msg);
	
}

int main(int argc, char **argv)
{
	std::cout << "Usage:" << std::endl <<
		"Press 'C' to spawn an AI Controlled player" << std::endl <<
		"Press 'Space' to spawn a User Controlled player" << std::endl <<
		"Use Left and Right arrows to control your character" << std::endl;
	ros::init(argc, argv, "game_node");
	GameNode node;
	// ros::spin();
	gl::gl_frontend glfe;
	Game g(200, 200, .1f);
	// std::cout << "Debug 1" << std::endl;
	glfe.init(g);
	// std::cout << "Debug 2" << std::endl;
	glfe.projectileScale = 1.f;
	glfe.playerScale = 1.f;
	glfe.enemyScale = 3.f;

	//Setup Scenario
	setupScenarioEasy(g);
	std::chrono::steady_clock::time_point start = std::chrono::steady_clock::now();
	std::chrono::milliseconds wait(1000/60);
	ros::Publisher game_state_pub = node.nh_.advertise<game::GameState>("game_state", 10);
	ros::Publisher pub_img = node.nh_.advertise<sensor_msgs::Image>("game_image", 1);

	while(!glfe.shouldClose(g))
	{
		g.tick();
		glfe.setupDraw();
		glfe.drawGame(g);
		glfe.finishDraw();
		publishImage(pub_img, 640, 480);
		glfe.update(g, g.getTimeStep());
		glfe.input(g);
		start += wait;
		std::this_thread::sleep_until(start);
		ros::spinOnce();
		if(!g.getPlayers().empty())
		{
			if (node.curr_dir > 0)
				g.getPlayers()[0]->x++;
			else if (node.curr_dir < 0)
				g.getPlayers()[0]->x--;
			// glfe.player->x--;
			
		}
		update_ros_game(g, game_state_pub);
	}
	glfe.finish(g);
	return 0;
}


void setupScenarioEasy(Game& g)
{
	//Setup Game Constants
	g.explosionTime = 2.f;
	g.explosionSize = 5.f;
	g.playerSpeed = .25f;

	//Construct Enemies
	Enemy& e = g.newEnemy(g.getWidth()/2, 10);
	e.minAngle = 3.14159f/2 - .3f;
	e.maxAngle = 3.14159f/2 + .3f;
	e.minForce = 50;
	e.maxForce = 51;
	e.firingRandomness = .1f;
	e.firingSpeed = 1e-2f;
}

void setupScenarioMedium(Game& g)
{
	//Setup Game Constants
	g.explosionTime = 2.f;
	g.explosionSize = 5.f;
	g.playerSpeed = .25f;

	//Construct Enemies
	Enemy& e = g.newEnemy(g.getWidth()/2, 10);
	e.minAngle = 3.14159f/2 - .3f;
	e.maxAngle = 3.14159f/2 + .3f;
	e.minForce = 50;
	e.maxForce = 51;
	e.firingSpeed = 5e-2f;
	e.firingRandomness = .6f;
}

void setupScenarioHard(Game& g)
{
	//Setup Game Constants
	g.explosionTime = 5.f;
	g.explosionSize = 5.f;
	g.playerSpeed = .25f;

	//Construct Enemies
	Enemy& e = g.newEnemy(g.getWidth()/2, 10);
	e.minAngle = 3.14159f/2 - .3f;
	e.maxAngle = 3.14159f/2 + .3f;
	e.minForce = 50;
	e.maxForce = 51;
	e.firingSpeed = 3e-2f;
	e.firingRandomness = .8f;
	e.turretSpeed = .15f;

	Enemy& e1 = g.newEnemy(g.getWidth()*.1f, 10);
	e1.minAngle = 3.14159f/2 - .5f;
	e1.maxAngle = 3.14159f/2;
	e1.minForce = 60;
	e1.maxForce = 61;
	e1.firingSpeed = 1e-1f;
	e1.firingRandomness = .0f;
	e1.turretSpeed = .05f;
}

void setupScenarioVeryHard(Game& g)
{
	//Setup Game Constants
	g.explosionTime = 1.f;
	g.explosionSize = 5.f;
	g.playerSpeed = .25f;

	//Construct Enemies
	Enemy& e = g.newEnemy(g.getWidth()/2, 10);
	e.minAngle = 3.14159f/2 - .05f;
	e.maxAngle = 3.14159f/2 + .05f;
	e.minForce = 100;
	e.maxForce = 101;
	e.firingSpeed = 8e-2f;
	e.firingRandomness = .4f;
	e.turretSpeed = 0.05f;

	Enemy& e1 = g.newEnemy(g.getWidth()*.1f, 10);
	e1.minAngle = 3.14159f/2 - .1f;
	e1.maxAngle = 3.14159f/2;
	e1.minForce = 100;
	e1.maxForce = 101;
	e1.firingSpeed = 1e-1f;
	e1.firingRandomness = .0f;
	e1.turretSpeed = .01f;

	Enemy& e2 = g.newEnemy(g.getWidth()*.9f, 10);
	e2.minAngle = 3.14159f/2;
	e2.maxAngle = 3.14159f/2 + .1f;
	e2.minForce = 100;
	e2.maxForce = 101;
	e2.firingSpeed = 5e-2f;
	e2.firingRandomness = .5f;
	e2.turretSpeed = .01f;
}

void setupScenarioImpossible(Game& g)
{
	//Setup Game Constants
	g.explosionTime = 4.f;
	g.explosionSize = 3.f;
	g.playerSpeed = 1.0f;

	//Construct Enemies
	Enemy& e = g.newEnemy(g.getWidth()/2, 10);
	e.minAngle = 3.14159f/2 - .3f;
	e.maxAngle = 3.14159f/2 + .3f;
	e.minForce = 50;
	e.maxForce = 51;
	e.firingSpeed = 8e-2f;
	e.firingRandomness = .8f;
	e.turretSpeed = .85f;

	Enemy& e1 = g.newEnemy(g.getWidth()*.1f, 10);
	e1.minAngle = 3.14159f/2 - .05f;
	e1.maxAngle = 3.14159f/2;
	e1.minForce = 200;
	e1.maxForce = 201;
	e1.firingSpeed = 1e-1f;
	e1.firingRandomness = .0f;
	e1.turretSpeed = .002f;

	Enemy& e2 = g.newEnemy(g.getWidth()*.9f, 10);
	e2.minAngle = 3.14159f/2;
	e2.maxAngle = 3.14159f/2 + .05f;
	e2.minForce = 200;
	e2.maxForce = 201;
	e2.firingSpeed = 1e-1f;
	e2.firingRandomness = .3f;
	e2.turretSpeed = .0025f;
}
