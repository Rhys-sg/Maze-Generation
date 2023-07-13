import graphics

def create_window(boarder_width, boarder_height, window_width, window_height):
    window = graphics.GraphWin("Screen", window_width, window_height)
    bounds = graphics.Rectangle(graphics.Point((window_width / 2) - (boarder_width / 2), (window_height / 2) + (boarder_height / 2)),
                                graphics.Point((window_width / 2) + (boarder_width / 2), (window_height / 2) - (boarder_height / 2)))
    bounds.draw(window)
    return window