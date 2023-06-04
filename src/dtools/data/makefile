
COMPILE_PATH = .temp
$(shell mkdir -p ${COMPILE_PATH})

RM = rm -rf

INCS = $(shell echo $(INCS_ROOT)|awk -F':' '{ for(i=1;i<=NF;i++) print $$i }')
TEST_ROOT = $(shell echo $(SRCS_ROOT)|awk -F':' '{ for(i=1;i<=NF;i++) print $$i }')
LFLAGS = $(shell echo $(lflags)|awk -F':' '{ for(i=1;i<=NF;i++) print $$i }')
LIBS_ROOT = $(shell echo $(libs_root)|awk -F':' '{ for(i=1;i<=NF;i++) print $$i }')
LIBS = $(shell echo $(libs)|awk -F':' '{ for(i=1;i<=NF;i++) print $$i }')
CXXFLAGS = $(shell echo $(cxxflags)|awk -F':'' { for(i=1;i<=NF;i++) print $$i }')

vpath %.cpp $(TEST_ROOT)
SRCS = $(foreach dir,$(TEST_ROOT),$(wildcard $(dir)/*.cpp))
OBJS = $(patsubst %.cpp, %.o, $(SRCS))

CLIB_OBJS = $(addprefix $(COMPILE_PATH)/,$(notdir $(OBJS)))

CXXFLAGS += $(INCS)
AFLAGS += -rcs

NAME = $(firstword $(shell uname -a))

$(COMPILE_PATH)/%.o: %.cpp
	$(CC) -c -fPIC $(CXXFLAGS) $< -o $@

main: $(CLIB_OBJS)
	$(CC) $(LFLAGS) $^ $(LIBS_ROOT) $(LIBS) -o $(TARGET)

lib: $(TARGET).a
$(TARGET).a: $(CLIB_OBJS)
	$(AR) $(AFLAGS) $@ $^ $(LIBS_ROOT) $(LIBS)

so: $(TARGET).so
$(TARGET).so: $(CLIB_OBJS)
	$(CC) $(LFLAGS) -o $@ $^ -fPIC -shared $(LIBS_ROOT) $(LIBS)

.PHONY: clean show

show:
	@echo $(NAME)
	@echo $(SRCS_ROOT)
	@echo $(TEST_ROOT)
	@echo $(SRCS)


clean:
	$(RM) $(COMPILE_PATH)
	$(RM) $(TARGET)
