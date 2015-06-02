
def creator(lst):
    print("da")
    room = open("templates/room.html", 'w')
    room.write("<form action='/completed/' method='POST'>")
    for x in range(10):
        for y in range(10):
            if (x,y) in lst:
                room.write("<input type='radio' name={} disabled>".format((x,y)))
            else:
                room.write("<input type='radio' name={}>".format((x,y)))
        room.write("<br>")
    room.write("<input type='submit' value='Submit'></form>")
    room.close()
