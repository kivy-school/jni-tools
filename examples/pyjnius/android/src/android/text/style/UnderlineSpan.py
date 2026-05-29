from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnderlineSpan"]

class UnderlineSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/UnderlineSpan"
    __javaconstructor__ = [("()V", False), ("(Landroid/os/Parcel;)V", False)]
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    updateDrawState = JavaMethod("(Landroid/text/TextPaint;)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSpanTypeId = JavaMethod("()I")