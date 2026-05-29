from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextAppearanceSpan"]

class TextAppearanceSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/TextAppearanceSpan"
    __javaconstructor__ = [("(Landroid/content/Context;I)V", False), ("(Ljava/lang/String;IILandroid/content/res/ColorStateList;Landroid/content/res/ColorStateList;)V", False), ("(Landroid/content/Context;II)V", False), ("(Landroid/os/Parcel;)V", False)]
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getTextStyle = JavaMethod("()I")
    getTextFontWeight = JavaMethod("()I")
    getLinkTextColor = JavaMethod("()Landroid/content/res/ColorStateList;")
    updateMeasureState = JavaMethod("(Landroid/text/TextPaint;)V")
    getFamily = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    getFontFeatureSettings = JavaMethod("()Ljava/lang/String;")
    getFontVariationSettings = JavaMethod("()Ljava/lang/String;")
    getLetterSpacing = JavaMethod("()F")
    getShadowColor = JavaMethod("()I")
    getShadowDx = JavaMethod("()F")
    getShadowDy = JavaMethod("()F")
    getShadowRadius = JavaMethod("()F")
    getTextLocales = JavaMethod("()Landroid/os/LocaleList;")
    getTextSize = JavaMethod("()I")
    getTypeface = JavaMethod("()Landroid/graphics/Typeface;")
    isElegantTextHeight = JavaMethod("()Z")
    updateDrawState = JavaMethod("(Landroid/text/TextPaint;)V")
    getTextColor = JavaMethod("()Landroid/content/res/ColorStateList;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSpanTypeId = JavaMethod("()I")