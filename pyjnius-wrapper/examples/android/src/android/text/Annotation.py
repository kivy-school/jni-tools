from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Annotation"]

class Annotation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/Annotation"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Landroid/os/Parcel;)V", False)]
    getSpanTypeId = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getKey = JavaMethod("()Ljava/lang/String;")
    getValue = JavaMethod("()Ljava/lang/String;")