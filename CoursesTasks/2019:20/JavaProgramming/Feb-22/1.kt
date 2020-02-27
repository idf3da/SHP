import kotlin.math.*

class Point(var _x: Double, var _y: Double) {
    var x = _x;
    var y = _y;

    fun dist(): Double {
        return sqrt(x.pow(2) + y.pow(2))
    }

    fun dist(pt: Point): Double {
        return sqrt((x - pt.x).pow(2) + (y - pt.y).pow(2))
    }
}

fun readDoubles() = readLine()!!.split(" ").map(it.toDouble())

fun main() {
    var (x1, y1) = readDoubles()
    var (x2, y2) = readDoubles()
    var pt1 = Point(x1, y1)
    var pt2 = Point(x2, y2)

}