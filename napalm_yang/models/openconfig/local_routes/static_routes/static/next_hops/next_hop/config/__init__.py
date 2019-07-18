# -*- coding: utf-8 -*-
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from collections import OrderedDict
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
elif six.PY2:
  import __builtin__

class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-local-routing - based on the path /local-routes/static-routes/static/next-hops/next-hop/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the next-hop
entry
  """
  __slots__ = ('_path_helper', '_extmethods', '__index','__next_hop','__metric','__recurse',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__index = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/local-routing', defining_module='openconfig-local-routing', yang_type='string', is_config=True)
    self.__next_hop = YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'DROP': {'@module': 'openconfig-local-routing', '@namespace': 'http://openconfig.net/yang/local-routing'}, 'oc-loc-rt:DROP': {'@module': 'openconfig-local-routing', '@namespace': 'http://openconfig.net/yang/local-routing'}, 'LOCAL_LINK': {'@module': 'openconfig-local-routing', '@namespace': 'http://openconfig.net/yang/local-routing'}, 'oc-loc-rt:LOCAL_LINK': {'@module': 'openconfig-local-routing', '@namespace': 'http://openconfig.net/yang/local-routing'}},),], is_leaf=True, yang_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/local-routing', defining_module='openconfig-local-routing', yang_type='union', is_config=True)
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/local-routing', defining_module='openconfig-local-routing', yang_type='uint32', is_config=True)
    self.__recurse = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="recurse", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/local-routing', defining_module='openconfig-local-routing', yang_type='boolean', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['local-routes', 'static-routes', 'static', 'next-hops', 'next-hop', 'config']

  def _get_index(self):
    """
    Getter method for index, mapped from YANG variable /local_routes/static_routes/static/next_hops/next_hop/config/index (string)

    YANG Description: An user-specified identifier utilised to uniquely reference
the next-hop entry in the next-hop list. The value of this
index has no semantic meaning other than for referencing
the entry.
    """
    return self.__index
      
  def _set_index(self, v, load=False):
    """
    Setter method for index, mapped from YANG variable /local_routes/static_routes/static/next_hops/next_hop/config/index (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_index() directly.

    YANG Description: An user-specified identifier utilised to uniquely reference
the next-hop entry in the next-hop list. The value of this
index has no semantic meaning other than for referencing
the entry.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/local-routing', defining_module='openconfig-local-routing', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """index must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/local-routing', defining_module='openconfig-local-routing', yang_type='string', is_config=True)""",
        })

    self.__index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_index(self):
    self.__index = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/local-routing', defining_module='openconfig-local-routing', yang_type='string', is_config=True)


  def _get_next_hop(self):
    """
    Getter method for next_hop, mapped from YANG variable /local_routes/static_routes/static/next_hops/next_hop/config/next_hop (union)

    YANG Description: The next-hop that is to be used for the static route
- this may be specified as an IP address, an interface
or a pre-defined next-hop type - for instance, DROP or
LOCAL_LINK. When this leaf is not set, and the interface-ref
value is specified for the next-hop, then the system should
treat the prefix as though it is directly connected to the
interface.
    """
    return self.__next_hop
      
  def _set_next_hop(self, v, load=False):
    """
    Setter method for next_hop, mapped from YANG variable /local_routes/static_routes/static/next_hops/next_hop/config/next_hop (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_next_hop is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_next_hop() directly.

    YANG Description: The next-hop that is to be used for the static route
- this may be specified as an IP address, an interface
or a pre-defined next-hop type - for instance, DROP or
LOCAL_LINK. When this leaf is not set, and the interface-ref
value is specified for the next-hop, then the system should
treat the prefix as though it is directly connected to the
interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'DROP': {'@module': 'openconfig-local-routing', '@namespace': 'http://openconfig.net/yang/local-routing'}, 'oc-loc-rt:DROP': {'@module': 'openconfig-local-routing', '@namespace': 'http://openconfig.net/yang/local-routing'}, 'LOCAL_LINK': {'@module': 'openconfig-local-routing', '@namespace': 'http://openconfig.net/yang/local-routing'}, 'oc-loc-rt:LOCAL_LINK': {'@module': 'openconfig-local-routing', '@namespace': 'http://openconfig.net/yang/local-routing'}},),], is_leaf=True, yang_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/local-routing', defining_module='openconfig-local-routing', yang_type='union', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """next_hop must be of a type compatible with union""",
          'defined-type': "openconfig-local-routing:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'DROP': {'@module': 'openconfig-local-routing', '@namespace': 'http://openconfig.net/yang/local-routing'}, 'oc-loc-rt:DROP': {'@module': 'openconfig-local-routing', '@namespace': 'http://openconfig.net/yang/local-routing'}, 'LOCAL_LINK': {'@module': 'openconfig-local-routing', '@namespace': 'http://openconfig.net/yang/local-routing'}, 'oc-loc-rt:LOCAL_LINK': {'@module': 'openconfig-local-routing', '@namespace': 'http://openconfig.net/yang/local-routing'}},),], is_leaf=True, yang_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/local-routing', defining_module='openconfig-local-routing', yang_type='union', is_config=True)""",
        })

    self.__next_hop = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_next_hop(self):
    self.__next_hop = YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'DROP': {'@module': 'openconfig-local-routing', '@namespace': 'http://openconfig.net/yang/local-routing'}, 'oc-loc-rt:DROP': {'@module': 'openconfig-local-routing', '@namespace': 'http://openconfig.net/yang/local-routing'}, 'LOCAL_LINK': {'@module': 'openconfig-local-routing', '@namespace': 'http://openconfig.net/yang/local-routing'}, 'oc-loc-rt:LOCAL_LINK': {'@module': 'openconfig-local-routing', '@namespace': 'http://openconfig.net/yang/local-routing'}},),], is_leaf=True, yang_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/local-routing', defining_module='openconfig-local-routing', yang_type='union', is_config=True)


  def _get_metric(self):
    """
    Getter method for metric, mapped from YANG variable /local_routes/static_routes/static/next_hops/next_hop/config/metric (uint32)

    YANG Description: A metric which is utilised to specify the preference of
the next-hop entry when it is injected into the RIB. The
lower the metric, the more preferable the prefix is. When
this value is not specified the metric is inherited from
the default metric utilised for static routes within the
network instance that the static routes are being
instantiated. When multiple next-hops are specified for a
static route, the metric is utilised to determine which of
the next-hops is to be installed in the RIB. When multiple
next-hops have the same metric (be it specified, or simply
the default) then these next-hops should all be installed
in the RIB
    """
    return self.__metric
      
  def _set_metric(self, v, load=False):
    """
    Setter method for metric, mapped from YANG variable /local_routes/static_routes/static/next_hops/next_hop/config/metric (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_metric() directly.

    YANG Description: A metric which is utilised to specify the preference of
the next-hop entry when it is injected into the RIB. The
lower the metric, the more preferable the prefix is. When
this value is not specified the metric is inherited from
the default metric utilised for static routes within the
network instance that the static routes are being
instantiated. When multiple next-hops are specified for a
static route, the metric is utilised to determine which of
the next-hops is to be installed in the RIB. When multiple
next-hops have the same metric (be it specified, or simply
the default) then these next-hops should all be installed
in the RIB
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/local-routing', defining_module='openconfig-local-routing', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """metric must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/local-routing', defining_module='openconfig-local-routing', yang_type='uint32', is_config=True)""",
        })

    self.__metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_metric(self):
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/local-routing', defining_module='openconfig-local-routing', yang_type='uint32', is_config=True)


  def _get_recurse(self):
    """
    Getter method for recurse, mapped from YANG variable /local_routes/static_routes/static/next_hops/next_hop/config/recurse (boolean)

    YANG Description: Determines whether the next-hop should be allowed to
be looked up recursively - i.e., via a RIB entry which has
been installed by a routing protocol, or another static route
- rather than needing to be connected directly to an
interface of the local system within the current network
instance. When the interface reference specified within the
next-hop entry is set (i.e., is not null) then forwarding is
restricted to being via the interface specified - and
recursion is hence disabled.
    """
    return self.__recurse
      
  def _set_recurse(self, v, load=False):
    """
    Setter method for recurse, mapped from YANG variable /local_routes/static_routes/static/next_hops/next_hop/config/recurse (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_recurse is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_recurse() directly.

    YANG Description: Determines whether the next-hop should be allowed to
be looked up recursively - i.e., via a RIB entry which has
been installed by a routing protocol, or another static route
- rather than needing to be connected directly to an
interface of the local system within the current network
instance. When the interface reference specified within the
next-hop entry is set (i.e., is not null) then forwarding is
restricted to being via the interface specified - and
recursion is hence disabled.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="recurse", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/local-routing', defining_module='openconfig-local-routing', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """recurse must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="recurse", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/local-routing', defining_module='openconfig-local-routing', yang_type='boolean', is_config=True)""",
        })

    self.__recurse = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_recurse(self):
    self.__recurse = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="recurse", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/local-routing', defining_module='openconfig-local-routing', yang_type='boolean', is_config=True)

  index = __builtin__.property(_get_index, _set_index)
  next_hop = __builtin__.property(_get_next_hop, _set_next_hop)
  metric = __builtin__.property(_get_metric, _set_metric)
  recurse = __builtin__.property(_get_recurse, _set_recurse)


  _pyangbind_elements = OrderedDict([('index', index), ('next_hop', next_hop), ('metric', metric), ('recurse', recurse), ])

