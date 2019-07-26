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

from . import defined_sets
from . import policy_definitions
class routing_policy(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-routing-policy - based on the path /routing-policy. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level container for all routing policy configuration
  """
  __slots__ = ('_path_helper', '_extmethods', '__defined_sets','__policy_definitions',)

  _yang_name = 'routing-policy'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__defined_sets = YANGDynClass(base=defined_sets.defined_sets, is_container='container', yang_name="defined-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    self.__policy_definitions = YANGDynClass(base=policy_definitions.policy_definitions, is_container='container', yang_name="policy-definitions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)

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
      return ['routing-policy']

  def _get_defined_sets(self):
    """
    Getter method for defined_sets, mapped from YANG variable /routing_policy/defined_sets (container)

    YANG Description: Predefined sets of attributes used in policy match
statements
    """
    return self.__defined_sets
      
  def _set_defined_sets(self, v, load=False):
    """
    Setter method for defined_sets, mapped from YANG variable /routing_policy/defined_sets (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_defined_sets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_defined_sets() directly.

    YANG Description: Predefined sets of attributes used in policy match
statements
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=defined_sets.defined_sets, is_container='container', yang_name="defined-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """defined_sets must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=defined_sets.defined_sets, is_container='container', yang_name="defined-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)""",
        })

    self.__defined_sets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_defined_sets(self):
    self.__defined_sets = YANGDynClass(base=defined_sets.defined_sets, is_container='container', yang_name="defined-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)


  def _get_policy_definitions(self):
    """
    Getter method for policy_definitions, mapped from YANG variable /routing_policy/policy_definitions (container)

    YANG Description: Enclosing container for the list of top-level policy
 definitions
    """
    return self.__policy_definitions
      
  def _set_policy_definitions(self, v, load=False):
    """
    Setter method for policy_definitions, mapped from YANG variable /routing_policy/policy_definitions (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_policy_definitions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_policy_definitions() directly.

    YANG Description: Enclosing container for the list of top-level policy
 definitions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=policy_definitions.policy_definitions, is_container='container', yang_name="policy-definitions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """policy_definitions must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=policy_definitions.policy_definitions, is_container='container', yang_name="policy-definitions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)""",
        })

    self.__policy_definitions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_policy_definitions(self):
    self.__policy_definitions = YANGDynClass(base=policy_definitions.policy_definitions, is_container='container', yang_name="policy-definitions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)

  defined_sets = __builtin__.property(_get_defined_sets, _set_defined_sets)
  policy_definitions = __builtin__.property(_get_policy_definitions, _set_policy_definitions)


  _pyangbind_elements = OrderedDict([('defined_sets', defined_sets), ('policy_definitions', policy_definitions), ])


from . import defined_sets
from . import policy_definitions
class routing_policy(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-routing-policy - based on the path /routing-policy. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level container for all routing policy configuration
  """
  __slots__ = ('_path_helper', '_extmethods', '__defined_sets','__policy_definitions',)

  _yang_name = 'routing-policy'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__policy_definitions = YANGDynClass(base=policy_definitions.policy_definitions, is_container='container', yang_name="policy-definitions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    self.__defined_sets = YANGDynClass(base=defined_sets.defined_sets, is_container='container', yang_name="defined-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)

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
      return ['routing-policy']

  def _get_defined_sets(self):
    """
    Getter method for defined_sets, mapped from YANG variable /routing_policy/defined_sets (container)

    YANG Description: Predefined sets of attributes used in policy match
statements
    """
    return self.__defined_sets
      
  def _set_defined_sets(self, v, load=False):
    """
    Setter method for defined_sets, mapped from YANG variable /routing_policy/defined_sets (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_defined_sets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_defined_sets() directly.

    YANG Description: Predefined sets of attributes used in policy match
statements
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=defined_sets.defined_sets, is_container='container', yang_name="defined-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """defined_sets must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=defined_sets.defined_sets, is_container='container', yang_name="defined-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)""",
        })

    self.__defined_sets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_defined_sets(self):
    self.__defined_sets = YANGDynClass(base=defined_sets.defined_sets, is_container='container', yang_name="defined-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)


  def _get_policy_definitions(self):
    """
    Getter method for policy_definitions, mapped from YANG variable /routing_policy/policy_definitions (container)

    YANG Description: Enclosing container for the list of top-level policy
 definitions
    """
    return self.__policy_definitions
      
  def _set_policy_definitions(self, v, load=False):
    """
    Setter method for policy_definitions, mapped from YANG variable /routing_policy/policy_definitions (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_policy_definitions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_policy_definitions() directly.

    YANG Description: Enclosing container for the list of top-level policy
 definitions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=policy_definitions.policy_definitions, is_container='container', yang_name="policy-definitions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """policy_definitions must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=policy_definitions.policy_definitions, is_container='container', yang_name="policy-definitions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)""",
        })

    self.__policy_definitions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_policy_definitions(self):
    self.__policy_definitions = YANGDynClass(base=policy_definitions.policy_definitions, is_container='container', yang_name="policy-definitions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)

  defined_sets = __builtin__.property(_get_defined_sets, _set_defined_sets)
  policy_definitions = __builtin__.property(_get_policy_definitions, _set_policy_definitions)


  _pyangbind_elements = OrderedDict([('defined_sets', defined_sets), ('policy_definitions', policy_definitions), ])


