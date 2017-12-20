#ifndef CONTROLLER_H
#define CONTROLLER_H
class Controller{
	public:
		bool states[6];
		int relay_on(int r);
		int relay_off(int r);
		int toggle_relay(int r);
		int reset_controller();
		bool get_status(int r);
};
#endif
