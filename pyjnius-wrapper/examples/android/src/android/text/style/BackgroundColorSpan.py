from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BackgroundColorSpan"]

class BackgroundColorSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/BackgroundColorSpan"
    __javaconstructor__ = [("(I)V", False), ("(Landroid/os/Parcel;)V", False)]
    getSpanTypeId = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getBackgroundColor = JavaMethod("()I")
    updateDrawState = JavaMethod("(Landroid/text/TextPaint;)V")
    toString = JavaMethod("()Ljava/lang/String;")