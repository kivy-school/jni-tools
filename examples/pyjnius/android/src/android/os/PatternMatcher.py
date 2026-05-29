from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PatternMatcher"]

class PatternMatcher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/PatternMatcher"
    __javaconstructor__ = [("(Landroid/os/Parcel;)V", False), ("(Ljava/lang/String;I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    PATTERN_ADVANCED_GLOB = JavaStaticField("I")
    PATTERN_LITERAL = JavaStaticField("I")
    PATTERN_PREFIX = JavaStaticField("I")
    PATTERN_SIMPLE_GLOB = JavaStaticField("I")
    PATTERN_SUFFIX = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    match = JavaMethod("(Ljava/lang/String;)Z")
    getType = JavaMethod("()I")
    getPath = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")