from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PropertyChangeListener"]

class PropertyChangeListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/beans/PropertyChangeListener"
    propertyChange = JavaMethod("(Ljava/beans/PropertyChangeEvent;)V")