from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class Mass(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/Mass"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Landroid/health/connect/datatypes/units/Mass;)I", False, False)])
    fromGrams = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/Mass;")
    getInGrams = JavaMethod("()D")

class Length(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/Length"
    fromMeters = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/Length;")
    getInMeters = JavaMethod("()D")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Landroid/health/connect/datatypes/units/Length;)I", False, False), ("(Ljava/lang/Object;)I", False, False)])

class BloodGlucose(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/BloodGlucose"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Landroid/health/connect/datatypes/units/BloodGlucose;)I", False, False)])
    fromMillimolesPerLiter = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/BloodGlucose;")
    getInMillimolesPerLiter = JavaMethod("()D")

class Power(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/Power"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Landroid/health/connect/datatypes/units/Power;)I", False, False)])
    fromWatts = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/Power;")
    getInWatts = JavaMethod("()D")

class Temperature(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/Temperature"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Landroid/health/connect/datatypes/units/Temperature;)I", False, False)])
    getInCelsius = JavaMethod("()D")
    fromCelsius = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/Temperature;")

class Percentage(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/Percentage"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Landroid/health/connect/datatypes/units/Percentage;)I", False, False)])
    getValue = JavaMethod("()D")
    fromValue = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/Percentage;")

class Volume(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/Volume"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Landroid/health/connect/datatypes/units/Volume;)I", False, False)])
    getInLiters = JavaMethod("()D")
    fromLiters = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/Volume;")

class TemperatureDelta(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/TemperatureDelta"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Landroid/health/connect/datatypes/units/TemperatureDelta;)I", False, False)])
    getInCelsius = JavaMethod("()D")
    fromCelsius = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/TemperatureDelta;")

class Velocity(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/Velocity"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Landroid/health/connect/datatypes/units/Velocity;)I", False, False)])
    fromMetersPerSecond = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/Velocity;")
    getInMetersPerSecond = JavaMethod("()D")

class Energy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/Energy"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Landroid/health/connect/datatypes/units/Energy;)I", False, False)])
    fromCalories = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/Energy;")
    getInCalories = JavaMethod("()D")

class Pressure(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/Pressure"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Landroid/health/connect/datatypes/units/Pressure;)I", False, False)])
    fromMillimetersOfMercury = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/Pressure;")
    getInMillimetersOfMercury = JavaMethod("()D")