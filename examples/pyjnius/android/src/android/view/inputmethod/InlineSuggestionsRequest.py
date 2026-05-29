from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InlineSuggestionsRequest"]

class InlineSuggestionsRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/InlineSuggestionsRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SUGGESTION_COUNT_UNLIMITED = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getHostPackageName = JavaMethod("()Ljava/lang/String;")
    getInlinePresentationSpecs = JavaMethod("()Ljava/util/List;")
    getInlineTooltipPresentationSpec = JavaMethod("()Landroid/widget/inline/InlinePresentationSpec;")
    getMaxSuggestionCount = JavaMethod("()I")
    getSupportedLocales = JavaMethod("()Landroid/os/LocaleList;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/InlineSuggestionsRequest$Builder"
        __javaconstructor__ = [("(Ljava/util/List;)V", False)]
        addInlinePresentationSpecs = JavaMethod("(Landroid/widget/inline/InlinePresentationSpec;)Landroid/view/inputmethod/InlineSuggestionsRequest$Builder;")
        setInlinePresentationSpecs = JavaMethod("(Ljava/util/List;)Landroid/view/inputmethod/InlineSuggestionsRequest$Builder;")
        setInlineTooltipPresentationSpec = JavaMethod("(Landroid/widget/inline/InlinePresentationSpec;)Landroid/view/inputmethod/InlineSuggestionsRequest$Builder;")
        setMaxSuggestionCount = JavaMethod("(I)Landroid/view/inputmethod/InlineSuggestionsRequest$Builder;")
        setSupportedLocales = JavaMethod("(Landroid/os/LocaleList;)Landroid/view/inputmethod/InlineSuggestionsRequest$Builder;")
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/inputmethod/InlineSuggestionsRequest$Builder;")
        build = JavaMethod("()Landroid/view/inputmethod/InlineSuggestionsRequest;")