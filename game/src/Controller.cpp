#include "Controller.h"
#include <cmath>
#include <iostream>
namespace mrsd
{
	void Controller::control(const mrsd::Game& g, float t)
	{
	}

	void Controller::createPlayer(Game& g)
	{
		if(p == 0)
		{
			p = new Player();
			p->dead = true;
		}
		if(p->dead)
		{
			p->dead = false;
			p->x = g.getWidth()/2;
			g.newPlayer(p);
		}
	}

	Prediction Controller::trackProjectile(const Projectile& p, const Game& g)
	{
		Prediction pred;
		return pred;
	}

	void Controller::determineSafeSpots(const Game& g)
	{
	}

	int Controller::pickSafeSpot(const Game& g)
	{
		return 0;
	}
}
