from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SimpleExpandableListAdapter"]

class SimpleExpandableListAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/SimpleExpandableListAdapter"
    __javaconstructor__ = [("(Landroid/content/Context;Ljava/util/List;I[Ljava/lang/String;[ILjava/util/List;I[Ljava/lang/String;[I)V", False), ("(Landroid/content/Context;Ljava/util/List;II[Ljava/lang/String;[ILjava/util/List;I[Ljava/lang/String;[I)V", False), ("(Landroid/content/Context;Ljava/util/List;II[Ljava/lang/String;[ILjava/util/List;II[Ljava/lang/String;[I)V", False)]
    getGroup = JavaMethod("(I)Ljava/lang/Object;")
    getChildId = JavaMethod("(II)J")
    getChildView = JavaMethod("(IIZLandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    getChildrenCount = JavaMethod("(I)I")
    getGroupCount = JavaMethod("()I")
    getGroupId = JavaMethod("(I)J")
    getGroupView = JavaMethod("(IZLandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    isChildSelectable = JavaMethod("(II)Z")
    newChildView = JavaMethod("(ZLandroid/view/ViewGroup;)Landroid/view/View;")
    newGroupView = JavaMethod("(ZLandroid/view/ViewGroup;)Landroid/view/View;")
    getChild = JavaMethod("(II)Ljava/lang/Object;")
    hasStableIds = JavaMethod("()Z")