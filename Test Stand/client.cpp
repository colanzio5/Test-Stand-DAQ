#include <ncurses.h>
#include "include/controller.h"

main() {
	
	WINDOW *w, *s, *t;
	char list[6][15] = { "Solenoid 1", "Solenoid 2", "Solenoid 3", "Solenoid 4", "Solenoid 5", "Solenoid 6" };
	char item[7];
	char item2[7];
	char item3[40];
	int ch, i = 0, width = 7;
	
	Controller con;

	con.reset_controller();

	con.toggle_relay(2);

	initscr();
	t = newwin( 3, 33, 1, 1 );
	box( t, 0, 0 );
	sprintf(item3, "%-6s", "    SDSURP Relay Controls");
	mvwprintw( t, i+1, 2, "%s", item3);

	w = newwin( 8, 14, 4, 1 );
	box( w, 0, 0 );
	
	for( i=0; i<6; i++ ) {
		if( i == 0 ) 
			wattron( w, A_STANDOUT );
		else
			wattroff( w, A_STANDOUT );
		sprintf(item, "%-7s",  list[i]);
		mvwprintw( w, i+1, 2, "%s", item );
	}

	s = newwin( 8, 14, 4, 20 );
	box( s, 0, 0 );

	for( i=0; i<6; i++ ) {
		char *state;
		if(con.get_status(i))
			state = "Open";
		else
			state = "Closed";
		sprintf(item2, "%-7s", state);
		mvwprintw( s, i+1, 2, "%s", item2 );
	}

	wrefresh( t );
	wrefresh( w );
	wrefresh( s );

	i = 0;
	noecho();
	keypad( w, TRUE );
	curs_set( 0 );
	
	while(( ch = wgetch(w)) != 'q'){ 
		
		sprintf(item, "%-7s",  list[i]); 
		mvwprintw( w, i+1, 2, "%s", item ); 
		switch( ch ) {
			case KEY_UP:
				i--;
				i = ( i<0 ) ? 5 : i;
				break;
			case KEY_DOWN:
				i++;
				i = ( i>5 ) ? 0 : i;
				break;
			case KEY_RIGHT:
				con.toggle_relay(i);
				char *state;
				if(con.get_status(i))
					state = "Open";
				else
					state = "Closed";
				sprintf(item2, "%-7s", state);
				mvwprintw( s, i+1, 2, "%s", item2);
				wrefresh(s);
				break;
		}
		wattron( w, A_STANDOUT );
				
		
		sprintf(item, "%-7s",  list[i]);
		mvwprintw( w, i+1, 2, "%s", item);
		wattroff( w, A_STANDOUT );
	}

	delwin( w );
	endwin();
}
