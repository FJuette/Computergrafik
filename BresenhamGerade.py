def gerade(xBeg, yBeg, xEnd, yEnd):
    deltaX = xEnd - xBeg;
    deltaY = yEnd - yBeg;
    x = xBeg;
    y = yBeg;

    n = 0;
    output(x, y, "", n);

    # Welche ist die schnelle Richtung?
    if deltaX >= deltaY:
        # Entlang der X-Achse
        en = abs(deltaX) / 2 - abs(deltaY);
        while x != xEnd:
            n += 1;
            x += sign(deltaX);
            if en < 0:
                # Y-Punkt setzen
                y += sign(deltaX);
            output(x, y, en * 2, n);
            # Entscheidungsvariable für den nächsten Punkt
            if en < 0:
                en = en + abs(deltaX) - abs(deltaY)
            else:
                en -= deltaY;
    else:
        # Entlang der Y-Achse
        en = abs(deltaY) / 2 - abs(deltaX);
        while y != yEnd:
            n += 1;
            y += sign(deltaY);
            if en < 0:
                # X-Punkt setzen
                x += sign(deltaX);
            output(x, y, en * 2, n);
            # Entscheidungsvariable für den nächsten Punkt
            if en < 0:
                en = en + abs(deltaY) - abs(deltaX)
            else:
                en -= deltaX;


def sign(x):
    if x >= 0:
        return 1;
    return -1;


def output(x, y, en, n):
    print("e(" + str(n) + "): " + str(en) +
          "\nx(" + str(n) + "): " + str(x) +
          "\ny(" + str(n) + "): " + str(y) +
          "\n-----------------");


if __name__ == '__main__':
    gerade(111, -113, 201, 65);