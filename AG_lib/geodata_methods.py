"""
This module contains custom functions to manipulate geophysical data.

OneTonTyler LLC
Written By: Tyler Singleton
04-01-2023
"""

## . . Necessary imports
import numpy as np
import pprint as pp


class Geodata:
    """The base class for storing geophysical data"""
    def __init__(self, rx, rz, sx, sz, dt, data):
        self.rx = rx  # Geophone receiver x_coordinate
        self.rz = rz  # Geophone receiver z_coordinate
        self.sx = sx  # Source x_coordinate
        self.sz = sz  # Source z_coordinate
        self.dt = dt  # Time resolution

        ## Calculated attributes
        self.data = np.ravel(self.data)                    # Geophone receiver data
        self.taxis = np.arange(self.data.size)*self.dt     # Time axis
        self.offset = self.get_offset([sx, sz], [rx, rz])  # Distance between source and receiver

    def print(self):
        """Prints general information about the class"""
        info = {
            'Coordinate': {'rx': self.rx, 'rz': self.rz},
            'Time delta': self.dt,
            'Data': self.data
        }

        pp.pprint(info)

    @staticmethod
    def get_offset(p1, p2):
        """ Calculate the euclidean distance between source and receiver

        :param p1: list
            Source coordinates
        :param p2: list
            Receiver coordinates
        :return: float
            The euclidean distance between two points
        """
        return np.sqrt(np.sum(np.diff([p1,p2], axis=0)**2))

    # noinspection PyUnresolvedReferences
    def read_synthetic_data(self, file_dir, name):
        syn_data = np.load(file_dir)

        for idx, trace in enumerate(self.f.data.T):
            args = {
                'sx': float(syn_data.f.sx),
                'sz': float(syn_data.f.sz),
                'name': f'{name}_Trace_{idx}',
                'dt': float(syn_data.f.dt),
                'rx': syn_data.f.rx[idx],
                'rz': syn_data.f.rz[idx],
                'data': trace,
            }