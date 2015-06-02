
def creator(lst, proj_id):
    room = open("website/templates/room.html", 'w')
    room.writelines("<form action='/completed/' method='POST'>")
    room.writelines("{% csrf_token %}")
    room.writelines('<input type="hidden" name="proj_id" value={}>'.format(proj_id))
    for x in range(10):
        for y in range(10):
            print("da")
            if (x,y) in lst:
                room.writelines("<input type='radio' name={} disabled>".format(x*10 + y))
            else:
                room.writelines("<input type='radio' name={}>".format(x*10 + y))
        room.writelines("<br>")
    room.writelines("<input type='submit' value='Submit'></form>")
    room.close()
