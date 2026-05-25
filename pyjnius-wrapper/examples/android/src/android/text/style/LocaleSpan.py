from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocaleSpan"]

class LocaleSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/LocaleSpan"
    __javaconstructor__ = [("(Ljava/util/Locale;)V", False), ("(Landroid/os/LocaleList;)V", False), ("(Landroid/os/Parcel;)V", False)]
    getSpanTypeId = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getLocale = JavaMethod("()Ljava/util/Locale;")
    getLocales = JavaMethod("()Landroid/os/LocaleList;")
    updateDrawState = JavaMethod("(Landroid/text/TextPaint;)V")
    updateMeasureState = JavaMethod("(Landroid/text/TextPaint;)V")
    toString = JavaMethod("()Ljava/lang/String;")