#pragma once

namespace mrsd
{
	struct Player
	{
		bool dead;
		float x;
		Player(): dead(true), x(0){}
	};
}
