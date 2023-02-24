//
//  File.swift
//  algorithmStudy
//
//  Created by 이의진 on 2022/07/01.
//

import Foundation

//
//  main.swift
//  makePoint
//
//  Created by 이의진 on 2022/07/01.
//

import Foundation

struct Point{
    var x : Double = 0
    var y : Double = 0
}


private func makePoint(centerPoint : Point, dataList : [Double]) -> [Point]{
    let pi = Double.pi
    var points : [Point] = []
    for i in 0...4{
        var point = Point(x: 0, y: 0)
        let angle : Double = (pi / 2) + Double(i) * (2/5) * pi
        point.x = centerPoint.x + dataList[i] * cos((pi / 2) + angle)
        point.y = centerPoint.y + dataList[i] * sin((pi / 2) + angle)
        points.append(point)
    }
    var averageDataPoint: Point = Point(x: 0, y: 0)
    for point in points{
        averageDataPoint.x += (point.x - centerPoint.x)
        averageDataPoint.y += (point.y - centerPoint.y)
    }
    averageDataPoint.x += centerPoint.x
    averageDataPoint.y += centerPoint.y
    points.append(averageDataPoint)
    return points
}

func solving(){
    let centerPoint = Point(x:400, y:400)
    let dataList : [Double] = [30, 40, 30, 20, 30]
    print(makePoint(centerPoint: centerPoint, dataList: dataList))
    
}

