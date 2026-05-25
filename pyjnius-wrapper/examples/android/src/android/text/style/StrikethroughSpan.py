from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StrikethroughSpan"]

class StrikethroughSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/StrikethroughSpan"
    __javaconstructor__ = [("()V", False), ("(Landroid/os/Parcel;)V", False)]
    getSpanTypeId = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    updateDrawState = JavaMethod("(Landroid/text/TextPaint;)V")
    toString = JavaMethod("()Ljava/lang/String;")