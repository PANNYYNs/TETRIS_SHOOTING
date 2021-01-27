def atk(gx,gy,ex,ey,sizex):
	if (gx >= ex and gx <= ex+sizex) and gy == ey:
		return True
	return False
