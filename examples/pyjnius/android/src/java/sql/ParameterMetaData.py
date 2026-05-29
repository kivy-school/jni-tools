from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ParameterMetaData"]

class ParameterMetaData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/ParameterMetaData"
    parameterNoNulls = JavaStaticField("I")
    parameterNullable = JavaStaticField("I")
    parameterNullableUnknown = JavaStaticField("I")
    parameterModeUnknown = JavaStaticField("I")
    parameterModeIn = JavaStaticField("I")
    parameterModeInOut = JavaStaticField("I")
    parameterModeOut = JavaStaticField("I")
    isNullable = JavaMethod("(I)I")
    getParameterType = JavaMethod("(I)I")
    getParameterTypeName = JavaMethod("(I)Ljava/lang/String;")
    getParameterClassName = JavaMethod("(I)Ljava/lang/String;")
    getParameterMode = JavaMethod("(I)I")
    getParameterCount = JavaMethod("()I")
    getScale = JavaMethod("(I)I")
    isSigned = JavaMethod("(I)Z")
    getPrecision = JavaMethod("(I)I")