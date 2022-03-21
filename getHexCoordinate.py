	def get_cell( self, ( x, y ) ):
		"""
		Identify the cell clicked in terms of row and column
		"""
		# Identify the square grid the click is in.
		row = math.floor( y / ( SQRT3 * self.radius ) )
		col = math.floor( x / ( 1.5 * self.radius ) )

		# Determine if cell outside cell centered in this grid.
		x = x - col * 1.5 * self.radius
		y = y - row * SQRT3 * self.radius

		# Transform row to match our hex coordinates, approximately
		row = row + math.floor( ( col + 1 ) / 2.0 )

		# Correct row and col for boundaries of a hex grid 
		if col % 2 == 0:
			if 	y < SQRT3 * self.radius / 2 and x < .5 * self.radius and \
				y < SQRT3 * self.radius / 2 - x:
				row, col = row - 1, col - 1
			elif y > SQRT3 * self.radius / 2 and x < .5 * self.radius and \
				y > SQRT3 * self.radius / 2 + x:
				row, col = row, col - 1
		else:
			if 	x < .5 * self.radius and abs( y - SQRT3 * self.radius / 2 ) < SQRT3 * self.radius / 2 - x:
				row, col = row - 1 , col - 1
			elif y < SQRT3 * self.radius / 2:
				row, col = row - 1, col


		return ( row, col ) if self.map.valid_cell( ( row, col ) ) else None
