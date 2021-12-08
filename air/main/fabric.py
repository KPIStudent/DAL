from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def update_model(self, obj, data):
        pass


class Product(ABC):
    @abstractmethod
    def update_obj(self, obj, data):
        pass


class StationUpdate(Creator):
    def update_model(self, station, data):
        return StationProduct().update_obj(station, data)


class ChronologyUpdate(Creator):
    def update_model(self, chronology, data):
        return ChronologyProduct().update_obj(chronology, data)


class StationProduct(Product):
    def update_obj(self, station, data):
        station.update(region=data[0]['region'],
                       pollution_percentage=data[0]['pollution_percentage'],
                       allowable_rate=data[0]['allowable_rate'],
                       chronology=data[0]['chronology'])


class ChronologyProduct(Product):
    def update_obj(self, chronology, data):
        chronology.update(last_update=data[0]['last_update'],
                          last_post=data[0]['last_post'],
                          post_periodicity=data[0]['post_periodicity '],
                          update_periodicity=data[0][' update_periodicity'])

