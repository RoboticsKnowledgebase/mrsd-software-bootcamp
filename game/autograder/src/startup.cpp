#include "glad/glad.h"
#include <GLFW/glfw3.h>
#include "Game.h"
#include "gl_frontend.h"
#include <iostream>
#include <chrono>
#include <thread>
#include <iostream>
#include <fstream>
#include "json.hpp"

using json = nlohmann::json;
using namespace mrsd;

void setupScenarioEasy(Game &);
void setupScenarioMedium(Game &);
void setupScenarioHard(Game &);
void setupScenarioVeryHard(Game &);
void setupScenarioImpossible(Game &);

int executeScenario(gl::gl_frontend &glfe, Game &g){
	int iterations = 0;
	while (iterations < (int) (90/g.getTimeStep()) && !g.playerDead)
	{
		g.tick();
		// glfe.setupDraw();
		// glfe.drawGame(g);
		// glfe.finishDraw();
		glfe.update(g, g.getTimeStep());
		iterations += 1;
	}
	return iterations;
}


int main(void)
{
	gl::gl_frontend glfe;
	Game g(200, 200, .1f);
	glfe.init(g);
	glfe.startai(g);

	glfe.projectileScale = 1.f;
	glfe.playerScale = 1.f;
	glfe.enemyScale = 3.f;

	std::function<void(Game &)> setupScenarios[] = {
        setupScenarioEasy,
        setupScenarioMedium,
        setupScenarioHard,
        setupScenarioVeryHard,
        setupScenarioImpossible
    };

	float score = 0;
	int maxLevelReached = 0;
	int totalIterations = 0;
	// time in seconds
	
	for(int i = 0; i < 5; i++){
		maxLevelReached = i;
		setupScenarios[i](g);
		std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
		int time_lasted = executeScenario(glfe, g);
		std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
		float timer = std::chrono::duration_cast<std::chrono::seconds>(end - begin).count();
		totalIterations += time_lasted;
		score += (maxLevelReached + 1) * time_lasted / timer;
		std::cout << "Score: " << score << std::endl;
		if(g.playerDead){
			break;
		}
	}
	
	

	std::string level = "";
	switch(maxLevelReached){
		case 0:
			level = "Easy";
			break;
		case 1:
			level = "Medium";
			break;
		case 2:
			level = "Hard";
			break;
		case 3:
			level = "Very Hard";
			break;
		case 4:
			level = "Impossible";
			break;
		default:
			level = "Easy";
			break;
	}
	std::cout << "Final Score: " << score << std::endl;
	std::cout << "Max Level Reached: " << level << std::endl;

	json j;
	// std::ofstream autograder_result("results.json");
	std::ofstream autograder_result("/autograder/results/results.json");

	json leaderboardArray = json::array();
	leaderboardArray.push_back({{"name", "Score"}, {"value", score}, {"order", "desc"}});
    leaderboardArray.push_back({{"name", "Maximum Level Reached"}, {"value", maxLevelReached}});

	j["leaderboard"] = leaderboardArray;
	if(score >= 2700){
		j["score"] = 5;
	}
	else{
		j["score"] = 0;
	}
	// if (timer < 90) // Fail
	// 	j["score"] = 0;
	// else // Success
	// 	j["score"] = 5;

	autograder_result << std::setw(4) << j << std::endl;

	return 0;
}

void setupScenarioEasy(Game &g)
{
	// Setup Game Constants
	g.explosionTime = 2.f;
	g.explosionSize = 5.f;
	g.playerSpeed = .25f;

	// Construct Enemies
	Enemy &e = g.newEnemy(g.getWidth() / 2, 10);
	e.minAngle = 3.14159f / 2 - .3f;
	e.maxAngle = 3.14159f / 2 + .3f;
	e.minForce = 50;
	e.maxForce = 51;
	e.firingRandomness = .1f;
	e.firingSpeed = 1e-2f;
}

void setupScenarioMedium(Game &g)
{
	// Setup Game Constants
	g.explosionTime = 2.f;
	g.explosionSize = 5.f;
	g.playerSpeed = .25f;

	// Construct Enemies
	Enemy &e = g.newEnemy(g.getWidth() / 2, 10);
	e.minAngle = 3.14159f / 2 - .3f;
	e.maxAngle = 3.14159f / 2 + .3f;
	e.minForce = 50;
	e.maxForce = 51;
	e.firingSpeed = 5e-2f;
	e.firingRandomness = .6f;
}

void setupScenarioHard(Game &g)
{
	// Setup Game Constants
	g.explosionTime = 5.f;
	g.explosionSize = 5.f;
	g.playerSpeed = .25f;

	// Construct Enemies
	Enemy &e = g.newEnemy(g.getWidth() / 2, 10);
	e.minAngle = 3.14159f / 2 - .3f;
	e.maxAngle = 3.14159f / 2 + .3f;
	e.minForce = 50;
	e.maxForce = 51;
	e.firingSpeed = 3e-2f;
	e.firingRandomness = .8f;
	e.turretSpeed = .15f;

	Enemy &e1 = g.newEnemy(g.getWidth() * .1f, 10);
	e1.minAngle = 3.14159f / 2 - .5f;
	e1.maxAngle = 3.14159f / 2;
	e1.minForce = 60;
	e1.maxForce = 61;
	e1.firingSpeed = 1e-1f;
	e1.firingRandomness = .0f;
	e1.turretSpeed = .05f;
}

void setupScenarioVeryHard(Game &g)
{
	// Setup Game Constants
	g.explosionTime = 1.f;
	g.explosionSize = 5.f;
	g.playerSpeed = .25f;

	// Construct Enemies
	Enemy &e = g.newEnemy(g.getWidth() / 2, 10);
	e.minAngle = 3.14159f / 2 - .05f;
	e.maxAngle = 3.14159f / 2 + .05f;
	e.minForce = 100;
	e.maxForce = 101;
	e.firingSpeed = 8e-2f;
	e.firingRandomness = .4f;
	e.turretSpeed = 0.05f;

	Enemy &e1 = g.newEnemy(g.getWidth() * .1f, 10);
	e1.minAngle = 3.14159f / 2 - .1f;
	e1.maxAngle = 3.14159f / 2;
	e1.minForce = 100;
	e1.maxForce = 101;
	e1.firingSpeed = 1e-1f;
	e1.firingRandomness = .0f;
	e1.turretSpeed = .01f;

	Enemy &e2 = g.newEnemy(g.getWidth() * .9f, 10);
	e2.minAngle = 3.14159f / 2;
	e2.maxAngle = 3.14159f / 2 + .1f;
	e2.minForce = 100;
	e2.maxForce = 101;
	e2.firingSpeed = 5e-2f;
	e2.firingRandomness = .5f;
	e2.turretSpeed = .01f;
}

void setupScenarioImpossible(Game &g)
{
	// Setup Game Constants
	g.explosionTime = 4.f;
	g.explosionSize = 3.f;
	g.playerSpeed = 1.0f;

	// Construct Enemies
	Enemy &e = g.newEnemy(g.getWidth() / 2, 10);
	e.minAngle = 3.14159f / 2 - .3f;
	e.maxAngle = 3.14159f / 2 + .3f;
	e.minForce = 50;
	e.maxForce = 51;
	e.firingSpeed = 8e-2f;
	e.firingRandomness = .8f;
	e.turretSpeed = .85f;

	Enemy &e1 = g.newEnemy(g.getWidth() * .1f, 10);
	e1.minAngle = 3.14159f / 2 - .05f;
	e1.maxAngle = 3.14159f / 2;
	e1.minForce = 200;
	e1.maxForce = 201;
	e1.firingSpeed = 1e-1f;
	e1.firingRandomness = .0f;
	e1.turretSpeed = .002f;

	Enemy &e2 = g.newEnemy(g.getWidth() * .9f, 10);
	e2.minAngle = 3.14159f / 2;
	e2.maxAngle = 3.14159f / 2 + .05f;
	e2.minForce = 200;
	e2.maxForce = 201;
	e2.firingSpeed = 1e-1f;
	e2.firingRandomness = .3f;
	e2.turretSpeed = .0025f;
}
