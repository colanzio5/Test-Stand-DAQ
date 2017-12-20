#include "include/controller.h"

const char *pi = "192.168.1.132";
bool states[6] = { false, false, false, false, false, false };

int Controller::relay_on( int r ){
	states[r] = true;
	return 0;
}
int Controller::relay_off( int r ){
	states[r] = false;
	return 0;
}
int Controller::toggle_relay( int r ){
	if(states[r]){
		relay_off(r);
	}
	else{
		relay_on(r);
	}
	return 0;
}
int Controller::reset_controller(){
	for(int i=0; i<6; i++){
		relay_off(i);
	}
	return 0;
}
bool Controller::get_status( int r ){
	return states[r];
}
