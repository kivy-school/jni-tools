from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    getWidgetType = JavaMethod("()I")
    getWidgetIndex = JavaMethod("()I")
    getWidgetRect = JavaMethod("()Landroid/graphics/Rect;")
    isReadOnly = JavaMethod("()Z")
    getTextValue = JavaMethod("()Ljava/lang/String;")
    getAccessibilityLabel = JavaMethod("()Ljava/lang/String;")
    isEditableText = JavaMethod("()Z")
    isMultiSelect = JavaMethod("()Z")
    isMultiLineText = JavaMethod("()Z")
    getMaxLength = JavaMethod("()I")
    getFontSize = JavaMethod("()F")
    getListItems = JavaMethod("()Ljava/util/List;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/pdf/models/FormWidgetInfo/Builder"
        __javaconstructor__ = [("(IILandroid/graphics/Rect;Ljava/lang/String;Ljava/lang/String;)V", False)]
        setReadOnly = JavaMethod("(Z)Landroid/graphics/pdf/models/FormWidgetInfo$Builder;")
        setEditableText = JavaMethod("(Z)Landroid/graphics/pdf/models/FormWidgetInfo$Builder;")
        setMultiSelect = JavaMethod("(Z)Landroid/graphics/pdf/models/FormWidgetInfo$Builder;")
        setMultiLineText = JavaMethod("(Z)Landroid/graphics/pdf/models/FormWidgetInfo$Builder;")
        setMaxLength = JavaMethod("(I)Landroid/graphics/pdf/models/FormWidgetInfo$Builder;")
        setFontSize = JavaMethod("(F)Landroid/graphics/pdf/models/FormWidgetInfo$Builder;")
        setListItems = JavaMethod("(Ljava/util/List;)Landroid/graphics/pdf/models/FormWidgetInfo$Builder;")
        build = JavaMethod("()Landroid/graphics/pdf/models/FormWidgetInfo;")