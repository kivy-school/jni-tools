from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocaleSpan"]

class LocaleSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/LocaleSpan"
    __javaconstructor__ = [("(Landroid/os/LocaleList;)V", False), ("(Ljava/util/Locale;)V", False), ("(Landroid/os/Parcel;)V", False)]
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    updateMeasureState = JavaMethod("(Landroid/text/TextPaint;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    getLocale = JavaMethod("()Ljava/util/Locale;")
    updateDrawState = JavaMethod("(Landroid/text/TextPaint;)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSpanTypeId = JavaMethod("()I")
    getLocales = JavaMethod("()Landroid/os/LocaleList;")