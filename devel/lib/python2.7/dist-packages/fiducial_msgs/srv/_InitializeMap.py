# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from fiducial_msgs/InitializeMapRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import fiducial_msgs.msg

class InitializeMapRequest(genpy.Message):
  _md5sum = "af3be60cc8712d87e234a795a01490e4"
  _type = "fiducial_msgs/InitializeMapRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """FiducialMapEntryArray fiducials

================================================================================
MSG: fiducial_msgs/FiducialMapEntryArray
FiducialMapEntry[] fiducials

================================================================================
MSG: fiducial_msgs/FiducialMapEntry
# pose of a fiducial
int32 fiducial_id
# translation
float64 x
float64 y
float64 z
# rotation
float64 rx
float64 ry
float64 rz

"""
  __slots__ = ['fiducials']
  _slot_types = ['fiducial_msgs/FiducialMapEntryArray']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       fiducials

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(InitializeMapRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.fiducials is None:
        self.fiducials = fiducial_msgs.msg.FiducialMapEntryArray()
    else:
      self.fiducials = fiducial_msgs.msg.FiducialMapEntryArray()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.fiducials.fiducials)
      buff.write(_struct_I.pack(length))
      for val1 in self.fiducials.fiducials:
        _x = val1
        buff.write(_get_struct_i6d().pack(_x.fiducial_id, _x.x, _x.y, _x.z, _x.rx, _x.ry, _x.rz))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.fiducials is None:
        self.fiducials = fiducial_msgs.msg.FiducialMapEntryArray()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.fiducials.fiducials = []
      for i in range(0, length):
        val1 = fiducial_msgs.msg.FiducialMapEntry()
        _x = val1
        start = end
        end += 52
        (_x.fiducial_id, _x.x, _x.y, _x.z, _x.rx, _x.ry, _x.rz,) = _get_struct_i6d().unpack(str[start:end])
        self.fiducials.fiducials.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.fiducials.fiducials)
      buff.write(_struct_I.pack(length))
      for val1 in self.fiducials.fiducials:
        _x = val1
        buff.write(_get_struct_i6d().pack(_x.fiducial_id, _x.x, _x.y, _x.z, _x.rx, _x.ry, _x.rz))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.fiducials is None:
        self.fiducials = fiducial_msgs.msg.FiducialMapEntryArray()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.fiducials.fiducials = []
      for i in range(0, length):
        val1 = fiducial_msgs.msg.FiducialMapEntry()
        _x = val1
        start = end
        end += 52
        (_x.fiducial_id, _x.x, _x.y, _x.z, _x.rx, _x.ry, _x.rz,) = _get_struct_i6d().unpack(str[start:end])
        self.fiducials.fiducials.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_i6d = None
def _get_struct_i6d():
    global _struct_i6d
    if _struct_i6d is None:
        _struct_i6d = struct.Struct("<i6d")
    return _struct_i6d
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from fiducial_msgs/InitializeMapResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class InitializeMapResponse(genpy.Message):
  _md5sum = "d41d8cd98f00b204e9800998ecf8427e"
  _type = "fiducial_msgs/InitializeMapResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
"""
  __slots__ = []
  _slot_types = []

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(InitializeMapResponse, self).__init__(*args, **kwds)

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
class InitializeMap(object):
  _type          = 'fiducial_msgs/InitializeMap'
  _md5sum = 'af3be60cc8712d87e234a795a01490e4'
  _request_class  = InitializeMapRequest
  _response_class = InitializeMapResponse
