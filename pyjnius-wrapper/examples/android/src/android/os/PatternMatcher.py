from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PatternMatcher"]

class PatternMatcher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/PatternMatcher"
    __javaconstructor__ = [("(Ljava/lang/String;I)V", False), ("(Landroid/os/Parcel;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    PATTERN_ADVANCED_GLOB = JavaStaticField("I")
    PATTERN_LITERAL = JavaStaticField("I")
    PATTERN_PREFIX = JavaStaticField("I")
    PATTERN_SIMPLE_GLOB = JavaStaticField("I")
    PATTERN_SUFFIX = JavaStaticField("I")
    getPath = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()I")
    match = JavaMethod("(Ljava/lang/String;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")