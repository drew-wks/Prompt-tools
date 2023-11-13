#Barfi is a visual flow-based programming librbary that provides a programming interface.
#Build a schema using barfi.Block to create blocks
#Execute the schema iwth barfi.ComputeEngine

from barfi import Block

#Defines Block 1: Start Block Type
start_block = Block(name='Input Block')
start_block.add_option(name="user_message", type="input", value="Input message here")
start_block.add_output(name="output")

def start_block_func(self):
   # self.set_interface(name='output', value="This text here is user input.")
    user_message = self.get_option("user_message") # this is not needed once we use a webapp-based form
    self.set_interface(name='output', value=user_message)

start_block.add_compute(start_block_func)


#Defines Block 2 a Transformer Block Type
transform_block = Block(name='Transformer Block')
transform_block.add_input(name="input1")
transform_block.add_input(name="input2")
transform_block.add_output(name="output")
transform_block.add_option(name="system_message", type="input", value="Put system message here")


def transform_func(self):
    in_1 = self.get_interface(name='input1')
    in_1 = self.get_interface(name='input2')
    system_message = self.get_option("system_message")

    # this is the actual transformation
    value = "Takes the input `" + in_1 + "` through AI using the system message `" + system_message + "`resulting in a " + "chat completion"

    self.set_interface(name='output', value=value)


transform_block.add_compute(transform_func)

#Defines Block 3 an Result Operator Block Type
result_block = Block(name='Result Block')
result_block.add_input(name="input")


def result_func(self):
    in_1 = self.get_interface(name='input')


result_block.add_compute(result_func)

process_blocks = [start_block, result_block, transform_block]