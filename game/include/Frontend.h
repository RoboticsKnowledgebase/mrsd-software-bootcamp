#pragma once
#include "Game.h"

namespace mrsd
{
	class Frontend
	{
		public:
			virtual void init(const Game& g) = 0;
			virtual void setupDraw() = 0;
			virtual void drawGame(const Game& g) = 0;
			virtual void finishDraw() = 0;
			virtual void update(const Game& g, float t) = 0;
			virtual void input(Game& g) = 0;
			virtual bool shouldClose(Game& g) = 0;
			virtual void finish(const Game& g) = 0;
	};

}
