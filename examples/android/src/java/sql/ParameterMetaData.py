from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ParameterMetaData"]

class ParameterMetaData(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/ParameterMetaData"
    parameterModeIn = JavaStaticField("I")
    parameterModeInOut = JavaStaticField("I")
    parameterModeOut = JavaStaticField("I")
    parameterModeUnknown = JavaStaticField("I")
    parameterNoNulls = JavaStaticField("I")
    parameterNullable = JavaStaticField("I")
    parameterNullableUnknown = JavaStaticField("I")
    getParameterCount = JavaMethod("()I")
    isNullable = JavaMethod("(I)I")
    isSigned = JavaMethod("(I)Z")
    getPrecision = JavaMethod("(I)I")
    getScale = JavaMethod("(I)I")
    getParameterType = JavaMethod("(I)I")
    getParameterTypeName = JavaMethod("(I)Ljava/lang/String;")
    getParameterClassName = JavaMethod("(I)Ljava/lang/String;")
    getParameterMode = JavaMethod("(I)I")