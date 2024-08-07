#pragma once
#include "Frontend.h"
#include "Game.h"
#include "glm/glm.hpp"
#include "GLMesh.h"
#include <GLFW/glfw3.h>
#include <vector>
namespace mrsd{
	struct Player;
	class Controller;
namespace gl{

	class gl_frontend : public Frontend
	{
		public:
			void init(const Game& g);
			void setupDraw();
			void drawGame(const Game& g);
			void update(const Game& g, float t);
			void finishDraw();
			bool shouldClose(Game& g);
			void input(Game& g);
			void startai(Game& g);
			void finish(const Game& g);
			float projectileScale;
			float playerScale, enemyScale;
			float iniExplosionScale, slopeExplosionScale;
			float explosionLifetime;
		private:
			Controller* controller;
			Player* player;
			float lastInput;
			GLFWwindow* window;
			glm::mat4 tform;
			glutils::GLMesh *circle;
			unsigned int prog;
	};
}
}
