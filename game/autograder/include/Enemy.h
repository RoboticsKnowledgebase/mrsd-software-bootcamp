#pragma once

namespace mrsd
{
	struct Enemy
	{
		int x, y;
		float turretAngle, minAngle, maxAngle, turretSpeed;
		int minForce, maxForce;
		float firingSpeed;
		float firingChance;
		float firingDelay;
		float firingRandomness;
		Enemy():x(0), y(0),
			turretAngle(0),
			minAngle(0),
			maxAngle(0),
			turretSpeed(.01),
			minForce(10),
			maxForce(11),
			firingSpeed(0),
			firingChance(0),
			firingDelay(0),
			firingRandomness(0)
		{}
	};
}
