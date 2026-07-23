PROG := qt-svg-composite
CPPFLAGS += $(shell pkg-config --cflags Qt6Svg)
LDLIBS   += $(shell pkg-config --libs Qt6Svg)

.PHONY: all generate clean
all: $(PROG)

generate: $(PROG)
	@./$(PROG) > ../qt/kvantum_generated_constants.py

clean:
	$(RM) $(PROG)
