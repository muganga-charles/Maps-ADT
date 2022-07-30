class Map :
    def __init__(self,key,value) :
        self.key = key
        self.value = value
        self._entryList = []
    def contains( self, key ) :
        for entry in self._entryList :
            if entry._key == key :
                return True
        return False
    def length( self ) :
        return len( self._entryList )

    def add( self, key, value ) :
        if self.contains( key ) :
            raise Exception( "Duplicate key" )
        self._entryList.append(Map( key, value ) )

    def remove( self, key ) :
        for entry in self._entryList :
            if entry._key == key :
                self._entryList.remove( entry )
                return
        assert False, "Invalid key"
    def  valueOf( self, key ) :
        for entry in self._entryList :
            if entry._key == key :
                return entry._value
        assert False, "Invalid key"

    def iterator(self):
        for entry in self._entryList:
            yield entry._key, entry._value
