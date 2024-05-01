#include "gl_frontend.h"
#include "glad/glad.h"
#include <GLFW/glfw3.h>
#include <iostream>
#include <vector>
#include <cstring>
#include "glutils.h"
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>
#include <glm/gtx/string_cast.hpp>
#include "Controller.h"

namespace mrsd{
namespace gl{



void gl_frontend::init(const Game& g)
{
	assert(glfwInit());
	window = glfwCreateWindow(640, 480, "Missile Defense", NULL, NULL);
	glfwMakeContextCurrent(window);
	gladLoadGLLoader((GLADloadproc) glfwGetProcAddress);

	prog = glutils::createShaderProgramFiles("/home/dvij/intro_to_rl/game_ws/src/game/shaders/vtxshader.glsl", "/home/dvij/intro_to_rl/game_ws/src/game/shaders/fragshader.glsl");
	std::cout << "Debug 3" << std::endl;
	glUseProgram(prog);
	circle = new glutils::GLMesh();
	circle->drawMode =  GL_TRIANGLE_FAN;
	int nPoints = 60;
	unsigned int *indices = new unsigned int[nPoints+2];
	float *vertices = new float[3*(nPoints+2)];
	float radPerPoint = 3.14159f*2.f/nPoints;
	for(int i = 0; i <= nPoints; i++)
	{
		vertices[3*i + 0] = std::cos(i * radPerPoint);
		vertices[3*i + 1] = std::sin(i * radPerPoint);
		vertices[3*i + 2] = 0;
		indices[i + 1] = i;
	}
	vertices[3*nPoints + 3] = vertices[3*nPoints + 4] = vertices[3*nPoints + 5] = 0.f;
	indices[0] = nPoints + 1;
	circle->buffer(vertices, 3*(nPoints+2), indices, nPoints + 2);
	tform = glm::ortho(0.f, (float)g.getWidth(), 0.0f, (float)g.getHeight(), -1.f, 1.f);
	player = new Player();
	player->dead = true;
	controller = new Controller();
}

void gl_frontend::setupDraw()
{
	int width, height;
	float aspect = 1.0f;
	int offX = 0, offY = 0;
	glfwGetFramebufferSize(window, &width, &height);
	float fbAR = (float)width/height;
	if(fbAR < aspect)
	{
		offY = (height - width*aspect)/2;
		height = width*aspect;
	}
	else if(fbAR > aspect)
	{
		offX = (width - height*1.f/aspect)/2;
		width = height*1.f/aspect;
	}
	glViewport(offX,offY,width,height);
	glClear(GL_COLOR_BUFFER_BIT);
}

void gl_frontend::drawGame(const Game& g)
{
	unsigned int tformLoc = glGetUniformLocation(prog, "tform");
	unsigned int colorLoc = glGetUniformLocation(prog, "color");
	glm::vec4 start, end;
	start = glm::vec4(1.f, 1.f, 0.0f, 1.0f);
	end = glm::vec4(1.0f, 0.0f, 0.0f, 1.0f);
	for(std::list<Explosion>::const_iterator it = g.getExplosions().begin(); it != g.getExplosions().end(); ++it)
	{
		const Explosion& gfx = *it;
		glm::mat4 obj_tform = tform;
		obj_tform *= glm::translate(glm::mat4(), glm::vec3(gfx.x, gfx.y,0));
		float scale = g.explosionSize;
		obj_tform *= glm::scale(glm::mat4(), glm::vec3(scale, scale, scale));
		glUniformMatrix4fv(tformLoc, 1, GL_FALSE, glm::value_ptr(obj_tform));
		glm::vec4 color = start + (end-start) * gfx.time / g.explosionTime;
		glUniform4f(colorLoc, color.r, color.g, color.b, color.a);
		circle->draw();
	}

	glUniform4f(colorLoc, 1.f, 1.f, 0.0f, 1.0f);
	for(std::list<Projectile>::const_iterator it = g.getProjectiles().begin();
			it != g.getProjectiles().end(); ++it)
	{
		const Projectile p = *it;
		glm::mat4 obj_tform = tform;
		obj_tform *= glm::translate(glm::mat4(), glm::vec3(p.x, p.y,0));
		float scale = projectileScale;
		obj_tform *= glm::scale(glm::mat4(), glm::vec3(scale, scale, scale));
		glUniformMatrix4fv(tformLoc, 1, GL_FALSE, glm::value_ptr(obj_tform));
		circle->draw();
	}
	glUniform4f(colorLoc, 1.f, 0.f, 0.0f, 1.0f);
	for(std::vector<Enemy>::const_iterator it = g.getEnemies().begin();
			it != g.getEnemies().end(); ++it)
	{
		const Enemy & e = *it;
		glm::mat4 obj_tform = tform;
		obj_tform *= glm::translate(glm::mat4(), glm::vec3(e.x, e.y, 0.f));
		float scale = enemyScale;
		obj_tform *= glm::scale(glm::mat4(), glm::vec3(scale, scale, scale));
		glUniformMatrix4fv(tformLoc, 1, GL_FALSE, glm::value_ptr(obj_tform));
		circle->draw();
	}
	glUniform4f(colorLoc, 0.f, 0.f, 1.0f, 1.0f);
	for(std::vector<Player*>::const_iterator it = g.getPlayers().begin();
			it != g.getPlayers().end(); ++it)
	{
		const Player & p = **it;
		glm::mat4 obj_tform = tform;
		obj_tform *= glm::translate(glm::mat4(), glm::vec3(p.x, 1.f, 0.f));
		float scale = playerScale;
		obj_tform *= glm::scale(glm::mat4(), glm::vec3(scale, scale, scale));
		glUniformMatrix4fv(tformLoc, 1, GL_FALSE, glm::value_ptr(obj_tform));
		circle->draw();
	}
}

void gl_frontend::finishDraw()
{
	glfwSwapBuffers(window);
}

bool gl_frontend::shouldClose(Game &g)
{
	glfwPollEvents();
	return glfwWindowShouldClose(window);
}

void gl_frontend::update(const Game& g, float t)
{
	controller->control(g, t);
}

void gl_frontend::input(Game& g)
{
	if(glfwGetKey(window, GLFW_KEY_SPACE))
	{
		if(player->dead)
		{
			player->x = g.getWidth()/2;
			player->dead = false;
			g.newPlayer(player);
		}
	}
	if(!player->dead)
	{
		if(glfwGetKey(window, GLFW_KEY_LEFT))
		{
			player->x--;
		}
		if(glfwGetKey(window, GLFW_KEY_RIGHT))
		{
			player->x++;
		}
	}
	if(glfwGetKey(window, GLFW_KEY_C))
	{
		controller->createPlayer(g);
	}
}

void gl_frontend::finish(const Game& g)
{
	glfwTerminate();
}

}
}
