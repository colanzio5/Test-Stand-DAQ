#include "include/controller.h"

class RelayController: public Controller {
	private:
		const char *pi = "http:\/\/192.168.1.132";
		bool states[6] = { false, false, false, false, false, false };
	public:
		int toggle_relay(int);
		int relay_on(int);
		int relay_off(int);
		int reset_controller();
		bool get_status(int);
};

int Controller::relay_on (int r) {
	//fetch http://$pi/$(r)on
	states[r] = true;
	return 0;
}

int Controller::relay_off (int r) {
	//fetch http://$pi/$(r)off
	states[r] = false;
	return 0;
}

int Controller::toggle_relay (int r) {
	if ( states[r] )
		relay_off(r);
	else
		relay_on(r);
	states[r] = !states[r];
	return 0;
}

int Controller::reset_controller() {
	for ( int i=0; i<6; i++ ){
		states[i] = false;
		relay_off(i);
	}
	return 0;
}

bool Controller::get_status (int r) {
	return states[r];
}
