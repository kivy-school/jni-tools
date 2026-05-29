from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SuggestionSpan"]

class SuggestionSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/SuggestionSpan"
    __javaconstructor__ = [("(Landroid/content/Context;[Ljava/lang/String;I)V", False), ("(Ljava/util/Locale;[Ljava/lang/String;I)V", False), ("(Landroid/content/Context;Ljava/util/Locale;[Ljava/lang/String;ILjava/lang/Class;)V", False), ("(Landroid/os/Parcel;)V", False)]
    ACTION_SUGGESTION_PICKED = JavaStaticField("Ljava/lang/String;")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_AUTO_CORRECTION = JavaStaticField("I")
    FLAG_EASY_CORRECT = JavaStaticField("I")
    FLAG_GRAMMAR_ERROR = JavaStaticField("I")
    FLAG_MISSPELLED = JavaStaticField("I")
    SUGGESTIONS_MAX_SIZE = JavaStaticField("I")
    SUGGESTION_SPAN_PICKED_AFTER = JavaStaticField("Ljava/lang/String;")
    SUGGESTION_SPAN_PICKED_BEFORE = JavaStaticField("Ljava/lang/String;")
    SUGGESTION_SPAN_PICKED_HASHCODE = JavaStaticField("Ljava/lang/String;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getUnderlineColor = JavaMethod("()I")
    getLocaleObject = JavaMethod("()Ljava/util/Locale;")
    getSuggestions = JavaMethod("()[Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getLocale = JavaMethod("()Ljava/lang/String;")
    updateDrawState = JavaMethod("(Landroid/text/TextPaint;)V")
    setFlags = JavaMethod("(I)V")
    getFlags = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSpanTypeId = JavaMethod("()I")