
COMPILE_PATH = ./temp
$(shell mkdir -p ${COMPILE_PATH})

RM  = @echo " RM  $@"; rm -rf
AR  = @echo " ar  $@"; $(AR)
CC = @echo "c++ $@"; $(CC)

INCS = $(INCS_ROOT)
SRCS = $(wildcard $(SRCS_ROOT)/*.cpp)
OBJS = $(patsubst %.cpp, %.o, $(notdir $(SRCS)))
CLIB_OBJS = $(addprefix $(COMPILE_PATH)/,$(LIB_OBJS))

CXXFLAGS += $(INCS)
AFLAGS += -rcs

LFLAGS ?= -O3 -Wall

TARGET ?= demo

NAME = $(firstword $(shell uname -a))

%.o: %.cpp
	$(CC) -c -fPIC $(CXXFLAGS) $^ -o $(COMPILE_PATH)/$@

main: $(TARGET)
$(TARGET): $(CLIB_OBJS)
	$(CC) $(LFLAGS) ^ -o $@

lib: $(TARGET).a
$(TARGET).a: $(CLIB_OBJS)
	$(AR) $(AFLAGS) $@ $^ $(LIBS)

so: $(TARGET).so
$(TARGET).so: $(CLIB_OBJS)
	$(CC) $(LFLAGS) -o $@ $^ -fPIC -shared $(LIBS)

show:
	@echo $(NAME)

clean:
	$(RM) $(COMPILE_PATH)
