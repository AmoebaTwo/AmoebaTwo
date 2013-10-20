#!/usr/bin/env python3

import pifacedigitalio

class Light:

	def __init__(self, b, i):
		self.board = b;
		self.index = i;

	def on(self):
		self.board.output_pins[self.index].turn_on();

	def off(self):
		self.board.output_pins[self.index].turn_off();

class Lights:

	def __init__(self, b):
		self.board = b;
		self.front = Light(self.board, 3);
		self.top = Light(self.board, 2);

	def blackout(self):
		self.front.off();
		self.top.off();

	def lightup(self):
		self.front.on();
		self.top.on();

class Move:

	def __init__(self, b):
		self.board = b;

	def forwards(self):
		self.board.output_pins[0].turn_on();
		self.board.output_pins[1].turn_on();
		
	def stop(self):
		self.board.output_pins[0].turn_off();
		self.board.output_pins[1].turn_off();
		
	def left(self):
		self.board.output_pins[0].turn_off();
		self.board.output_pins[1].turn_on();
		
	def right(self):
		self.board.output_pins[0].turn_on();
		self.board.output_pins[1].turn_off();

class InputListener:

	def __init__(self, b):
		self.board = b;
		self.listener = pifacedigitalio.InputEventListener(chip=self.board);
		self.inited = False;

	def register(self, port, fn):
		if self.inited:
			return;
		self.inited = True;
		self.listener.register(port, pifacedigitalio.IODIR_FALLING_EDGE, fn);
		self.listener.activate();

	def unregister(self):
		if not self.inited:
			return;
		self.inited = False;
		self.listener.deactivate();

class AmoebaTwo:
	
	def __init__(self):
		pifacedigitalio.init();
		self.board = pifacedigitalio.PiFaceDigital();
		self.lights = Lights(self.board);
		self.move = Move(self.board);

	def registerListener(self, port, fn):
		listener = InputListener(self.board);
		listener.register(port, fn);
		return listener;		

