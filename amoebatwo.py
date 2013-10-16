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


class AmoebaTwo:
	
	def __init__(self):
		pifacedigitalio.init();
		self.board = pifacedigitalio.PiFaceDigital();
		self.lights = Lights(self.board);
		self.move = Move(self.board);

	def __del__(self):
		pifacedigitalio.deinit();
	
