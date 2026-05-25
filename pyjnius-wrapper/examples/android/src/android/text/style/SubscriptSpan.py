from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SubscriptSpan"]

class SubscriptSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/SubscriptSpan"
    __javaconstructor__ = [("()V", False), ("(Landroid/os/Parcel;)V", False)]
    getSpanTypeId = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    updateDrawState = JavaMethod("(Landroid/text/TextPaint;)V")
    updateMeasureState = JavaMethod("(Landroid/text/TextPaint;)V")
    toString = JavaMethod("()Ljava/lang/String;")