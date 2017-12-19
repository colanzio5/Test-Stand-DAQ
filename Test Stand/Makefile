IDIR =./include
CC=gcc
CFLAGS=-I$(IDIR)

ODIR=obj
LDIR =./lib

LIBS=-lm -lncurses

_DEPS = controller.h
DEPS = $(patsubst %,$(IDIR)/%,$(_DEPS))

_OBJ = client.o controller.o
OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))


$(ODIR)/%.o: %.cpp $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

client: $(OBJ)
	gcc -o $@ $^ $(CFLAGS) $(LIBS)

.PHONY: clean

clean:
	rm -f client $(ODIR)/*.o *~ core $(INCDIR)/*~
