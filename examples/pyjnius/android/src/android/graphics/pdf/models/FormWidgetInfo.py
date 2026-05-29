from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FormWidgetInfo"]

class FormWidgetInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/models/FormWidgetInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    WIDGET_TYPE_CHECKBOX = JavaStaticField("I")
    WIDGET_TYPE_COMBOBOX = JavaStaticField("I")
    WIDGET_TYPE_LISTBOX = JavaStaticField("I")
    WIDGET_TYPE_PUSHBUTTON = JavaStaticField("I")
    WIDGET_TYPE_RADIOBUTTON = JavaStaticField("I")
    WIDGET_TYPE_SIGNATURE = JavaStaticField("I")
    WIDGET_TYPE_TEXTFIELD = JavaStaticField("I")
    WIDGET_TYPE_UNKNOWN = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getWidgetType = JavaMethod("()I")
    isMultiLineText = JavaMethod("()Z")
    getMaxLength = JavaMethod("()I")
    isEditableText = JavaMethod("()Z")
    getWidgetIndex = JavaMethod("()I")
    getFontSize = JavaMethod("()F")
    getWidgetRect = JavaMethod("()Landroid/graphics/Rect;")
    isMultiSelect = JavaMethod("()Z")
    getAccessibilityLabel = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getListItems = JavaMethod("()Ljava/util/List;")
    getTextValue = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    isReadOnly = JavaMethod("()Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/pdf/models/FormWidgetInfo$Builder"
        __javaconstructor__ = [("(IILandroid/graphics/Rect;Ljava/lang/String;Ljava/lang/String;)V", False)]
        setMultiLineText = JavaMethod("(Z)Landroid/graphics/pdf/models/FormWidgetInfo$Builder;")
        setMultiSelect = JavaMethod("(Z)Landroid/graphics/pdf/models/FormWidgetInfo$Builder;")
        setFontSize = JavaMethod("(F)Landroid/graphics/pdf/models/FormWidgetInfo$Builder;")
        setListItems = JavaMethod("(Ljava/util/List;)Landroid/graphics/pdf/models/FormWidgetInfo$Builder;")
        setEditableText = JavaMethod("(Z)Landroid/graphics/pdf/models/FormWidgetInfo$Builder;")
        setMaxLength = JavaMethod("(I)Landroid/graphics/pdf/models/FormWidgetInfo$Builder;")
        setReadOnly = JavaMethod("(Z)Landroid/graphics/pdf/models/FormWidgetInfo$Builder;")
        build = JavaMethod("()Landroid/graphics/pdf/models/FormWidgetInfo;")