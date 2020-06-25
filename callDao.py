from call import Call
import pg8000
import os

class CallDao : 
    def __init__(self) :
        # initialize database connection 
        self.con = pg8000.connect(
                user=os.environ['DB_USER'], 
                database=os.environ['DB'], 
                password=os.environ['DB_PASSWORD'])

    def storeCall(self, c, extended_address, formatted_address, lat, lon) :
        self.con.run("INSERT INTO call (hash_code, date, precinct, address, status_code, location_lat, location_lon, extended_address, geom)" +
        "VALUES (:hash_code, TO_TIMESTAMP(:date, 'YYYY-MM-DD HH24:MI:SS'), :precinct, :address, :status_code, :location_lat, :location_lon, :extended_address, ST_SetSRID( ST_Point( :plon, :plat), 4326))" +
        " ON CONFLICT (hash_code) DO UPDATE " +
        " SET date=TO_TIMESTAMP(:date, 'YYYY-MM-DD HH24:MI:SS')," +
        " precinct=:precinct," +
        " address=:address," +
        " status_code=:status_code," +
        " location_lat=:location_lat," + 
        " location_lon=:location_lon," +
        " extended_address=:extended_address," + 
        " geom=ST_SetSRID( ST_Point( :plon, :plat), 4326)", 
        hash_code=c.getHashCode(), date=c.getCallDate(), precinct=c.getPrecinct(), address=c.getAddress(), status_code=c.getStatusCode(), location_lat=lat, location_lon=lon, extended_address=str(extended_address), plon=lon, plat=lat)

        self.con.commit()
        return 

    