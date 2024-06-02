#include "Controller.h"
#include <cmath>
#include <iostream>
namespace mrsd
{
	void Controller::control(const mrsd::Game& g, float t)
	{
		determineSafeSpots(g);
		std::vector<Player *> all_players = g.getPlayers();
		if(all_players.size() != 0){
			// all_players.front()->x = -(pred.x - g.getWidth());
			Player * player = all_players.front();
			// std::cout << (int) player->x << " " << pickSafeSpot(g) << std::endl;
			int safespot = pickSafeSpot(g);
			int curloc = (int) player->x;
			// player->x = pickSafeSpot(g);
			if(safespot != curloc){
				if(safespot < curloc){
					player->x -= g.playerSpeed;
				}
				else{
					player->x += g.playerSpeed;
				}
				
			}
			
		}
		// std::cout<<"Controlled" << std::endl;
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
		float gravity = (g.getGravity());
		pred.t = (-sqrt(4 * pow(p.vy, 2) - 8 * gravity * p.y)  - 2 * (p.vy))/ (2 * gravity);
		pred.x = p.x + p.vx * pred.t;
		// std::cout << "Positions | " << p.x  << " " << p.y << std::endl;
		// std::cout << "Velocities | " << p.vx  << " " << p.vy << std::endl;
		// std::cout << "(predictions) | "<< pred.t << "  " << pred.x  <<  " " <<  p.x << std::endl;
		return pred;
	}

	void Controller::determineSafeSpots(const Game& g)
	{	
		std::list <Projectile> projectiles = g.getProjectiles();
		for(int i = 0; i < g.getWidth(); i++){
			safeSpots[i] = 1;

		}
		auto front = projectiles.begin();
		for(int i = 0; i < projectiles.size(); i++)
		{	
			std::advance(front, i);
			
			pred = trackProjectile(*front, g);
			// safeSpots[(int) pred.x] = 0;
			for(int k = -g.explosionSize - 2; k < g.explosionSize + 3; k++){
				safeSpots[(int) (pred.x + g.getWidth() + k) % g.getWidth()] = 0;
			}
			
		}

		
	}

	int Controller::pickSafeSpot(const Game& g)
	{	
		if(g.getPlayers().size() != 0){
			int p1 = (int) p->x;
			int p2 = (int) p->x;

			while(safeSpots[p1] == 0 && safeSpots[p2] == 0){
				p1--;
				p2++;
				if(p1 == 0){
					p1 = g.getWidth();
				}
				if(p2 == g.getWidth()){
					p2 = 0;
				}
			}
			// std::cout << p->x << " " << p1 << " " <<p2 << std::endl;;
			
			// std::cout << safeSpots[(int)p->x] << " " << safeSpots[p1] << " " <<safeSpots[p2] <<std::endl;;
			if(safeSpots[p1] == 0){
				return p2;
			}
			return p1;
		}
		
	}
}