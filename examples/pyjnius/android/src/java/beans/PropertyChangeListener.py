from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PropertyChangeListener"]

class PropertyChangeListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/beans/PropertyChangeListener"
    propertyChange = JavaMethod("(Ljava/beans/PropertyChangeEvent;)V")